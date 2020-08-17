open OUnit2
open Rotting_oranges

let tests = "test suite for rotting oranges" >::: [
    "the process completes"     >:: (fun _ -> assert_equal  4 ( rottingOranges [[2;1;1];[1;1;0];[0;1;1]] ) );
    "the process never starts"  >:: (fun _ -> assert_equal  0 ( rottingOranges [[2;0]] ) );
    "the process cant complete" >:: (fun _ -> assert_equal (-1) ( rottingOranges [[2;1;1];[0;1;1];[1;0;1]] ) );
]

let _ = run_test_tt_main tests
