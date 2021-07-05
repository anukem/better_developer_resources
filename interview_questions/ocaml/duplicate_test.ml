open OUnit2
open Duplicate

let tests = "duplicate tests" >::: [
  "1"     >:: (fun _ -> assert_equal  [1;1;1;1;1;1] ( duplicate [1;1;1] ) );
  "2"     >:: (fun _ -> assert_equal  [1;1] ( duplicate [1] ) );
]

let _ = run_test_tt_main tests
