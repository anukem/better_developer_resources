open OUnit2
open Condense_list

let tests = "test suite for condensing a flattened list" >::: [
    "1"     >:: (fun _ -> assert_equal  [[1;1;1;1];[2;2]] ( condense_list [1;1;1;1;2;2] ) );
]

let _ = run_test_tt_main tests
