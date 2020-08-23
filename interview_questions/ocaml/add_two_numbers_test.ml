open OUnit2
open Add_two_numbers

let tests = "test suite for adding two lists together" >::: [
    "standard case 1"     >:: (fun _ -> assert_equal  [7;0;8] ( add_two_numbers [2;4;3] [5;6;4] ) );
    "two numbers with different sizes"     >:: (fun _ -> assert_equal  [0;0;7] ( add_two_numbers [9;9;6] [1] ) );
]

let _ = run_test_tt_main tests

