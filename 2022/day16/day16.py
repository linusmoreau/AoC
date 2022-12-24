from typing import *
from collections import deque


class Valve:
    def __init__(self, name: str, flow: int, leads: List[str]):
        self.name = name
        self.flow = flow
        self.leads = leads
        self.essential: Dict = {}

    def __repr__(self):
        return "Valve(" + self.name + ")"


def read_file():
    f = open("input.txt", "r")
    valves = {}
    for line in f:
        s = line.strip()
        parts = s.split()
        name = parts[1]
        flow = int(parts[4].strip(";").split("=")[1])
        leads = ""
        for i in range(9, len(parts)):
            leads += parts[i]
        leads = leads.split(",")
        valves[name] = Valve(name, flow, leads)
    f.close()
    return valves


def get_results(start):
    cache = {}
    results = []
    process = deque()
    process.append(start)
    while len(process) > 0:
        valve, path, n, tot = process.popleft()
        serial = (valve.name, tuple(sorted(path)))
        try:
            if cache[serial] >= tot:
                continue
        except KeyError:
            cache[serial] = tot
        tasks = len(process)
        for v, d in valve.essential.items():
            if v.flow > 0 and v.name not in path:
                if n - d <= 0:
                    results.append((tot, set(path)))
                else:
                    left = n - (d + 1)
                    process.append((v, path + [v.name], left, tot + left * v.flow))
        if len(process) == tasks:
            results.append((tot, set(path)))
    return results


if __name__ == "__main__":
    valves = read_file()
    must_visit = {"AA": valves["AA"]}
    for valve in valves.values():
        if valve.flow > 0:
            must_visit[valve.name] = valve.flow

    for valve in valves.values():
        if valve.name == "AA" or valve.flow > 0:
            visited = set()
            to_visit = deque()
            to_visit.append((valve, 0))

            while len(to_visit) > 0:
                cur, n = to_visit.popleft()
                visited.add(cur)
                if (cur.name == "AA" or cur.flow > 0) and n > 0:
                    valve.essential[cur] = n
                for v in cur.leads:
                    if valves[v] not in visited:
                        to_visit.append((valves[v], n + 1))

    results = get_results((valves["AA"], [], 30, 0))
    print("Part 1:", max(results, key=lambda x: x[0]))

    results = get_results((valves["AA"], [], 26, 0))
    results.sort(reverse=True)
    best = 0
    for i in range(len(results) - 1):
        if results[i][0] + results[i + 1][0] < best:
            break
        for j in range(i + 1, len(results)):
            s = results[i][0] + results[j][0]
            if s < best:
                break
            if len(results[i][1].intersection(results[j][1])) == 0 and s > best:
                best = s
    print("Part 2:", best)
