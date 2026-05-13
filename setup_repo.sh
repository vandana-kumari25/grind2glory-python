#!/bin/bash

# ==========================================
# Grind2Glory 150 Python Repository Generator
# ==========================================

REPO_NAME="grind2glory-python"

echo "Creating repository structure..."

# Assets
mkdir -p assets/{banners,diagrams,screenshots}

# Templates
mkdir -p templates
touch templates/binary_search_template.py
touch templates/bfs_template.py
touch templates/dfs_template.py
touch templates/sliding_window_template.py
touch templates/union_find_template.py
touch templates/dp_template.py

# Notes
mkdir -p notes
touch notes/time_complexities.md
touch notes/interview_patterns.md
touch notes/python_tricks.md
touch notes/problem_solving_approach.md

# Main Categories
mkdir -p arrays_hashing
mkdir -p two_pointers
mkdir -p sliding_window
mkdir -p stack
mkdir -p binary_search
mkdir -p linked_list
mkdir -p trees
mkdir -p tries
mkdir -p heap_priority_queue
mkdir -p backtracking
mkdir -p graphs
mkdir -p advanced_graphs
mkdir -p dynamic_programming_1d
mkdir -p dynamic_programming_2d
mkdir -p greedy
mkdir -p intervals
mkdir -p math_geometry
mkdir -p bit_manipulation

# Arrays & Hashing
touch arrays_hashing/contains_duplicate.py
touch arrays_hashing/valid_anagram.py
touch arrays_hashing/two_sum.py
touch arrays_hashing/group_anagrams.py
touch arrays_hashing/top_k_frequent_elements.py
touch arrays_hashing/product_of_array_except_self.py
touch arrays_hashing/valid_sudoku.py
touch arrays_hashing/encode_and_decode_strings.py
touch arrays_hashing/longest_consecutive_sequence.py

# Two Pointers
touch two_pointers/valid_palindrome.py
touch two_pointers/two_sum_ii.py
touch two_pointers/three_sum.py
touch two_pointers/container_with_most_water.py
touch two_pointers/trapping_rain_water.py

# Sliding Window
touch sliding_window/best_time_to_buy_sell_stock.py
touch sliding_window/longest_substring_without_repeating.py
touch sliding_window/longest_repeating_character_replacement.py
touch sliding_window/permutation_in_string.py
touch sliding_window/minimum_window_substring.py
touch sliding_window/sliding_window_maximum.py

# Stack
touch stack/valid_parentheses.py
touch stack/min_stack.py
touch stack/evaluate_reverse_polish_notation.py
touch stack/generate_parentheses.py
touch stack/daily_temperatures.py
touch stack/car_fleet.py
touch stack/largest_rectangle_histogram.py

# Binary Search
touch binary_search/binary_search.py
touch binary_search/search_2d_matrix.py
touch binary_search/koko_eating_bananas.py
touch binary_search/find_min_rotated_sorted_array.py
touch binary_search/search_rotated_sorted_array.py
touch binary_search/time_based_key_value_store.py
touch binary_search/median_two_sorted_arrays.py

# Linked List
touch linked_list/reverse_linked_list.py
touch linked_list/merge_two_sorted_lists.py
touch linked_list/reorder_list.py
touch linked_list/remove_nth_node.py
touch linked_list/copy_list_random_pointer.py
touch linked_list/add_two_numbers.py
touch linked_list/linked_list_cycle.py
touch linked_list/find_duplicate_number.py
touch linked_list/lru_cache.py
touch linked_list/merge_k_sorted_lists.py
touch linked_list/reverse_nodes_k_group.py

# Tests
mkdir -p tests
touch tests/test_arrays_hashing.py
touch tests/test_graphs.py
touch tests/test_dp.py
touch tests/test_trees.py

# Utils
mkdir -p utils
touch utils/tree_node.py
touch utils/linked_list.py
touch utils/graph_helpers.py
touch utils/input_parser.py

# Populate requirements.txt
cat <<EOL > requirements.txt
pytest
black
isort
EOL

# Populate .gitignore
cat <<EOL > .gitignore
__pycache__/
*.pyc
.env
.vscode/
.idea/
.DS_Store
EOL

# Basic README
cat <<EOL > README.md
# Grind2Glory 150 Python Solutions

🚀 Python solutions for Grind2Glory 150 with optimized approaches,
clean code, explanations, and interview-focused patterns.

## Topics Covered
- Arrays & Hashing
- Trees
- Graphs
- Dynamic Programming
- Greedy
- Backtracking
- Bit Manipulation

## Run Tests

\`\`\`bash
pytest
\`\`\`
EOL

echo "======================================"
echo "Repository structure created successfully!"
echo "Location: $(pwd)"
echo "======================================"