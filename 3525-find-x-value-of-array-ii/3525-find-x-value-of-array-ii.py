class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)

        if k == 1:
            return [n - q[2] for q in queries]

        size = 1 << (n - 1).bit_length()
        N = size << 1
        P = [1] * N
        C = [[0] * N for _ in range(k)]

        for i, x in enumerate(nums, size):
            r = x % k
            P[i] = r
            C[r][i] = 1

        result = []

        if k == 2:
            C0, C1 = C

            def pull(i):
                l = i << 1
                r = l | 1
                if P[l] == 0:
                    P[i] = 0
                    C0[i] = C0[l] + C0[r] + C1[r]
                    C1[i] = C1[l]
                else:
                    P[i] = P[r]
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C1[r]

            for i in range(size - 1, 0, -1):
                pull(i)

            for idx, val, start, x in queries:
                pos = size + idx
                r = val & 1
                if P[pos] != r:
                    old = P[pos]
                    P[pos] = r
                    C[old][pos] = 0
                    C[r][pos] = 1
                    pos >>= 1
                    while pos:
                        pull(pos)
                        pos >>= 1

                if start == 0:
                    result.append((C0[1], C1[1])[x])
                    continue

                i = start
                block = i & -i
                c_idx = (size + i) // block
                a_p = P[c_idx]
                a_c0 = C0[c_idx]
                a_c1 = C1[c_idx]
                i += block

                while i < size:
                    block = i & -i
                    c_idx = (size + i) // block
                    r_p = P[c_idx]
                    r_c0 = C0[c_idx]
                    r_c1 = C1[c_idx]

                    if a_p == 0:
                        a_p = 0
                        a_c0 += r_c0 + r_c1
                    else:
                        a_p = r_p
                        a_c0 += r_c0
                        a_c1 += r_c1
                    i += block

                result.append((a_c0, a_c1)[x])

        elif k == 3:
            C0, C1, C2 = C

            def pull(i):
                l = i << 1
                r = l | 1
                pa = P[l]
                if pa == 0:
                    P[i] = 0
                    C0[i] = C0[l] + C0[r] + C1[r] + C2[r]
                    C1[i] = C1[l]
                    C2[i] = C2[l]
                elif pa == 1:
                    P[i] = P[r]
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C1[r]
                    C2[i] = C2[l] + C2[r]
                else:
                    P[i] = (P[r] * 2) % 3
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C2[r]
                    C2[i] = C2[l] + C1[r]

            for i in range(size - 1, 0, -1):
                pull(i)

            for idx, val, start, x in queries:
                pos = size + idx
                r = val % 3
                if P[pos] != r:
                    old = P[pos]
                    P[pos] = r
                    C[old][pos] = 0
                    C[r][pos] = 1
                    pos >>= 1
                    while pos:
                        pull(pos)
                        pos >>= 1

                if start == 0:
                    result.append((C0[1], C1[1], C2[1])[x])
                    continue

                i = start
                block = i & -i
                c_idx = (size + i) // block
                a_p = P[c_idx]
                a_c0 = C0[c_idx]
                a_c1 = C1[c_idx]
                a_c2 = C2[c_idx]
                i += block

                while i < size:
                    block = i & -i
                    c_idx = (size + i) // block
                    r_p = P[c_idx]
                    r_c0 = C0[c_idx]
                    r_c1 = C1[c_idx]
                    r_c2 = C2[c_idx]

                    if a_p == 0:
                        a_p = 0
                        a_c0 += r_c0 + r_c1 + r_c2
                    elif a_p == 1:
                        a_p = r_p
                        a_c0 += r_c0
                        a_c1 += r_c1
                        a_c2 += r_c2
                    else:
                        a_p = (r_p * 2) % 3
                        n_c0 = a_c0 + r_c0
                        n_c1 = a_c1 + r_c2
                        n_c2 = a_c2 + r_c1
                        a_c0, a_c1, a_c2 = n_c0, n_c1, n_c2
                    i += block

                result.append((a_c0, a_c1, a_c2)[x])

        elif k == 4:
            C0, C1, C2, C3 = C

            def pull(i):
                l = i << 1
                r = l | 1
                pa = P[l]
                if pa == 0:
                    P[i] = 0
                    C0[i] = C0[l] + C0[r] + C1[r] + C2[r] + C3[r]
                    C1[i] = C1[l]
                    C2[i] = C2[l]
                    C3[i] = C3[l]
                elif pa == 1:
                    P[i] = P[r]
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C1[r]
                    C2[i] = C2[l] + C2[r]
                    C3[i] = C3[l] + C3[r]
                elif pa == 2:
                    P[i] = (P[r] * 2) % 4
                    C0[i] = C0[l] + C0[r] + C2[r]
                    C1[i] = C1[l]
                    C2[i] = C2[l] + C1[r] + C3[r]
                    C3[i] = C3[l]
                else:
                    P[i] = (P[r] * 3) % 4
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C3[r]
                    C2[i] = C2[l] + C2[r]
                    C3[i] = C3[l] + C1[r]

            for i in range(size - 1, 0, -1):
                pull(i)

            for idx, val, start, x in queries:
                pos = size + idx
                r = val & 3
                if P[pos] != r:
                    old = P[pos]
                    P[pos] = r
                    C[old][pos] = 0
                    C[r][pos] = 1
                    pos >>= 1
                    while pos:
                        pull(pos)
                        pos >>= 1

                if start == 0:
                    result.append((C0[1], C1[1], C2[1], C3[1])[x])
                    continue

                i = start
                block = i & -i
                c_idx = (size + i) // block
                a_p = P[c_idx]
                a_c0 = C0[c_idx]
                a_c1 = C1[c_idx]
                a_c2 = C2[c_idx]
                a_c3 = C3[c_idx]
                i += block

                while i < size:
                    block = i & -i
                    c_idx = (size + i) // block
                    r_p = P[c_idx]
                    r_c0 = C0[c_idx]
                    r_c1 = C1[c_idx]
                    r_c2 = C2[c_idx]
                    r_c3 = C3[c_idx]

                    if a_p == 0:
                        a_p = 0
                        a_c0 += r_c0 + r_c1 + r_c2 + r_c3
                    elif a_p == 1:
                        a_p = r_p
                        a_c0 += r_c0
                        a_c1 += r_c1
                        a_c2 += r_c2
                        a_c3 += r_c3
                    elif a_p == 2:
                        a_p = (r_p * 2) % 4
                        n_c0 = a_c0 + r_c0 + r_c2
                        n_c1 = a_c1
                        n_c2 = a_c2 + r_c1 + r_c3
                        n_c3 = a_c3
                        a_c0, a_c1, a_c2, a_c3 = n_c0, n_c1, n_c2, n_c3
                    else:
                        a_p = (r_p * 3) % 4
                        n_c0 = a_c0 + r_c0
                        n_c1 = a_c1 + r_c3
                        n_c2 = a_c2 + r_c2
                        n_c3 = a_c3 + r_c1
                        a_c0, a_c1, a_c2, a_c3 = n_c0, n_c1, n_c2, n_c3
                    i += block

                result.append((a_c0, a_c1, a_c2, a_c3)[x])

        else:
            C0, C1, C2, C3, C4 = C

            def pull(i):
                l = i << 1
                r = l | 1
                pa = P[l]
                if pa == 0:
                    P[i] = 0
                    C0[i] = C0[l] + C0[r] + C1[r] + C2[r] + C3[r] + C4[r]
                    C1[i] = C1[l]
                    C2[i] = C2[l]
                    C3[i] = C3[l]
                    C4[i] = C4[l]
                elif pa == 1:
                    P[i] = P[r]
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C1[r]
                    C2[i] = C2[l] + C2[r]
                    C3[i] = C3[l] + C3[r]
                    C4[i] = C4[l] + C4[r]
                elif pa == 2:
                    P[i] = (P[r] * 2) % 5
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C3[r]
                    C2[i] = C2[l] + C1[r]
                    C3[i] = C3[l] + C4[r]
                    C4[i] = C4[l] + C2[r]
                elif pa == 3:
                    P[i] = (P[r] * 3) % 5
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C2[r]
                    C2[i] = C2[l] + C4[r]
                    C3[i] = C3[l] + C1[r]
                    C4[i] = C4[l] + C3[r]
                else:
                    P[i] = (P[r] * 4) % 5
                    C0[i] = C0[l] + C0[r]
                    C1[i] = C1[l] + C4[r]
                    C2[i] = C2[l] + C3[r]
                    C3[i] = C3[l] + C2[r]
                    C4[i] = C4[l] + C1[r]

            for i in range(size - 1, 0, -1):
                pull(i)

            for idx, val, start, x in queries:
                pos = size + idx
                r = val % 5
                if P[pos] != r:
                    old = P[pos]
                    P[pos] = r
                    C[old][pos] = 0
                    C[r][pos] = 1
                    pos >>= 1
                    while pos:
                        pull(pos)
                        pos >>= 1

                if start == 0:
                    result.append((C0[1], C1[1], C2[1], C3[1], C4[1])[x])
                    continue

                i = start
                block = i & -i
                c_idx = (size + i) // block
                a_p = P[c_idx]
                a_c0 = C0[c_idx]
                a_c1 = C1[c_idx]
                a_c2 = C2[c_idx]
                a_c3 = C3[c_idx]
                a_c4 = C4[c_idx]
                i += block

                while i < size:
                    block = i & -i
                    c_idx = (size + i) // block
                    r_p = P[c_idx]
                    r_c0 = C0[c_idx]
                    r_c1 = C1[c_idx]
                    r_c2 = C2[c_idx]
                    r_c3 = C3[c_idx]
                    r_c4 = C4[c_idx]

                    if a_p == 0:
                        a_p = 0
                        a_c0 += r_c0 + r_c1 + r_c2 + r_c3 + r_c4
                    elif a_p == 1:
                        a_p = r_p
                        a_c0 += r_c0
                        a_c1 += r_c1
                        a_c2 += r_c2
                        a_c3 += r_c3
                        a_c4 += r_c4
                    elif a_p == 2:
                        a_p = (r_p * 2) % 5
                        n_c0 = a_c0 + r_c0
                        n_c1 = a_c1 + r_c3
                        n_c2 = a_c2 + r_c1
                        n_c3 = a_c3 + r_c4
                        n_c4 = a_c4 + r_c2
                        a_c0, a_c1, a_c2, a_c3, a_c4 = n_c0, n_c1, n_c2, n_c3, n_c4
                    elif a_p == 3:
                        a_p = (r_p * 3) % 5
                        n_c0 = a_c0 + r_c0
                        n_c1 = a_c1 + r_c2
                        n_c2 = a_c2 + r_c4
                        n_c3 = a_c3 + r_c1
                        n_c4 = a_c4 + r_c3
                        a_c0, a_c1, a_c2, a_c3, a_c4 = n_c0, n_c1, n_c2, n_c3, n_c4
                    else:
                        a_p = (r_p * 4) % 5
                        n_c0 = a_c0 + r_c0
                        n_c1 = a_c1 + r_c4
                        n_c2 = a_c2 + r_c3
                        n_c3 = a_c3 + r_c2
                        n_c4 = a_c4 + r_c1
                        a_c0, a_c1, a_c2, a_c3, a_c4 = n_c0, n_c1, n_c2, n_c3, n_c4
                    i += block

                result.append((a_c0, a_c1, a_c2, a_c3, a_c4)[x])

        return result