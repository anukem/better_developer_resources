open Fizzbuzz
open OUnit2

let tests = "test suite for buzz and fizz" >::: [
    "no fizz or buzz"      >:: (fun _ -> assert_equal ["1";"2"] ( fizz_buzz 2 ) );
    "fizz no buzz"      >:: (fun _ -> assert_equal ["1";"2"; "fizz"] ( fizz_buzz 3 ) );
    "fizz, buzz, but not fizzbuzz"      >:: (fun _ -> assert_equal ["1";"2"; "fizz"; "4"; "buzz"] ( fizz_buzz 5 ) );
    "fizz, buzz, AND fizzbuzz"      >:: (fun _ -> assert_equal
["1"; "2"; "fizz"; "4"; "buzz"; "fizz"; "7"; "8"; "fizz"; "buzz"; "11"; "fizz";
 "13"; "14"; "FizzBuzz"]
 ( fizz_buzz 15 ) );
]

let _ = run_test_tt_main tests
