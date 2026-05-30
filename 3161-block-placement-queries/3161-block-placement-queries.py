class Solution:
    def getResults(self, queries):

        # Upper bound on any position value that can appear in a query
        MAX_POS = min(5 * 10**4, len(queries) * 3)

        # Sentinel obstacles at 0 and MAX_POS so every real position
        # always has a left neighbor and a right neighbor — no edge cases
        obstacles = SortedList([0, MAX_POS])

        # ── Phase 1a: insert every obstacle upfront ────────────────────
        # We process queries in reverse later (removals are easier than
        # insertions). To enable that, we insert ALL type-1 obstacles now
        # so we can build the gap structure once over the full list.
        for query in queries:
            if query[0] == 1:
                obstacles.add(query[1])

        # ── Phase 1b: build the suffix-max gap structure ───────────────
        # suffix_max_gaps stores (right_endpoint, gap_size) entries, but
        # ONLY when that gap is strictly larger than every gap to its right.
        # This lets us answer "biggest gap reachable at or before X?" in
        # O(log n) with a single bisect.
        suffix_max_gaps = SortedList()
        suffix_max_gaps.add((0, 0))  # dummy anchor at the left boundary

        running_max = 0
        for left, right in pairwise(obstacles):
            gap_size = right - left
            if gap_size > running_max:
                # This gap is a new left-to-right maximum — worth recording
                suffix_max_gaps.add((right, gap_size))
                running_max = gap_size

        # ── Phase 2: replay queries in reverse ────────────────────────
        answers = []
        for query in reversed(queries):

            if query[0] == 1:
                # ── Type-1 (reversed): remove obstacle ────────────────
                pos = query[1]
                idx            = obstacles.index(pos)
                left_neighbor  = obstacles[idx - 1]
                right_neighbor = obstacles[idx + 1]
                obstacles.remove(pos)

                # The two gaps on either side of pos merge into one
                merged_gap = right_neighbor - left_neighbor

                # Remove any suffix_max_gaps entries that are now dominated:
                # anything between pos and right_neighbor with size <= merged_gap
                # is irrelevant — the new bigger gap covers it
                insert_idx = suffix_max_gaps.bisect_left((pos, 0))
                while insert_idx < len(suffix_max_gaps) and \
                      suffix_max_gaps[insert_idx][1] <= merged_gap:
                    suffix_max_gaps.pop(insert_idx)

                # Only insert the merged gap if it beats the entry to its left
                if suffix_max_gaps[insert_idx - 1][1] < merged_gap:
                    suffix_max_gaps.add((right_neighbor, merged_gap))

            else:
                # ── Type-2: answer the query ───────────────────────────
                _, pos, size_needed = query

                # Nearest obstacle at or to the left of the person's position
                left_obstacle = obstacles[obstacles.bisect_right(pos) - 1]

                # The person fits if EITHER:
                #   (a) the immediate gap between them and left_obstacle is big enough
                fits_in_local_gap = (pos - left_obstacle) >= size_needed

                #   (b) there's a larger gap somewhere further left they could use
                best_gap_to_left = suffix_max_gaps[
                    suffix_max_gaps.bisect_right((left_obstacle, math.inf)) - 1
                ][1]
                fits_in_earlier_gap = best_gap_to_left >= size_needed

                answers.append(fits_in_local_gap or fits_in_earlier_gap)

        # answers were collected in reverse query order — flip them back
        answers.reverse()
        return answers