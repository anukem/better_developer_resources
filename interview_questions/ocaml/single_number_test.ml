open OUnit2
open Single_number

let tests = "testing single number" >::: [
    "one triplet"                     >:: (fun _ -> assert_equal 2 (single_number 2 [1;1;1;2]) );
    "unique number is in the middle"  >:: (fun _ -> assert_equal 2 (single_number 2 [1;2;1;1]) );
    "multiple triplets"               >:: (fun _ -> assert_equal 2 (single_number 2 [4;1;2;1;1;4;4]) );
]

let _ = run_test_tt_main tests
