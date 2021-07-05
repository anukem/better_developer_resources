open OUnit2
open Replicate

let tests = "replicate tests" >::: [
  "1"     >:: (fun _ -> assert_equal  [1;1;1;1;1;1] ( replicate [1;1;1] 2 ) );
  "2"     >:: (fun _ -> assert_equal  [1;1;2;2] ( replicate [1; 2] 2 ) );
]

let _ = run_test_tt_main tests
