open OUnit2
open Intersection_of_two_arrays

let tests = "testing intersection of two arrays" >::: [
    "one element matches"             >:: (fun _ -> assert_equal [2] (intersection_of_two_arrays [4;2] [1;1;1;2]) );
    "multiple elements match"         >:: (fun _ -> assert_equal [2;3] (intersection_of_two_arrays [3;2] [1;3;1;2]) );
    "no elements match"               >:: (fun _ -> assert_equal [] (intersection_of_two_arrays [4;8] [1;1;1;2]) );
]

let _ = run_test_tt_main tests
