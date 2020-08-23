open OUnit2
open Mergesort

let tests = "test suite for merging lists" >::: [
    "the lists are empty"     >:: (fun _ -> assert_equal  [] ( merge_sort [] [] ) );
    "only one has an element"     >:: (fun _ -> assert_equal  [1] ( merge_sort [] [1] ) );
    "both have elements"     >:: (fun _ -> assert_equal [1; 2; 2; 3; 3; 4; 5; 5; 6; 7] ( merge_sort [2;3;3;5;6;7] [1;2;4;5] ) );
]

let _ = run_test_tt_main tests

