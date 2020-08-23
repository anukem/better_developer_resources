open OUnit2
open Cheapest_flights

let tests = "test suite for cheapest flights within k stops" >::: [
    "list drops two things"  >:: (fun _ -> assert_equal 200 (cheapest_flights [(0, 1, 100); (1,2,100); (0, 2, 500)] 0 2 1) );
]

let _ = run_test_tt_main tests
