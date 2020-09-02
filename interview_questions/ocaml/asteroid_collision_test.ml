open OUnit2
open Asteroid_collision

let rec print_list = function
[] -> "\n"
| e::l -> (string_of_int e) ^ " " ^ print_list l

let tests = "test suite for asteroids" >::: [
    "one gets crushed"  >:: (fun _ -> assert_equal [5;10] (asteroid_collision [5;10;-5]) );
    "left wins"  >:: (fun _ -> assert_equal [-100;1] (asteroid_collision [5;10;-5;-100;1]) ~printer:print_list );
]

let _ = run_test_tt_main tests
