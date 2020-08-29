open Find_equal_sum
open OUnit2

let tests = "test suite for finding rqual subset partitions in a list" >::: [
    "sum is possible"      >:: (fun _ -> assert_equal true ( find_equal_sum [1;5;11;5] ) );
    "sum is not possible"      >:: (fun _ -> assert_equal false ( find_equal_sum [1;2;4;4] ) );
]

let _ = run_test_tt_main tests
