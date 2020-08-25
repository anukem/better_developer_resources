open OUnit2
open Cheapest_flights

let tests = "test suite for cheapest flights within k stops" >::: [
    "shortest path requires one stop"  >:: (fun _ -> assert_equal 200 (cheapest_flights [(0, 1, 100); (1,2,100); (0, 2, 500)] 0 2 1) );
    "shortest path has no stops"  >:: (fun _ -> assert_equal 500 (cheapest_flights [(0, 1, 100); (1,2,100); (0, 2, 500)] 0 2 0) );
    "there is no path"  >:: (fun _ -> assert_equal (-1) (cheapest_flights [(0, 6, 100); (1,2,100); (0, 3, 500)] 0 2 1) );
    "one stop needed, but one that goes nowhere"  >:: (fun _ -> assert_equal 300 (cheapest_flights [(0,3,100);(1,2,100);(0,2,300)] 0 2 1) );
]
let _ = run_test_tt_main tests
