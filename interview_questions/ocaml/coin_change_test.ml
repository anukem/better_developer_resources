open Coin_change
open OUnit2

let tests = "test suite for coin change" >::: [
    "obama"                    >:: (fun _ -> assert_equal 2 ( coin_change [1;2;5;10] 11 ) );
    "you can make change"      >:: (fun _ -> assert_equal 3 ( coin_change [1;2;5] 11 ) );
    "you can't make change"    >:: (fun _ -> assert_equal (-1) ( coin_change [2] 3 ) );
    "the change is 7 from 3 and 4"    >:: (fun _ -> assert_equal 2 ( coin_change [1;3;4;5] 7 ) );
]

let _ = run_test_tt_main tests

