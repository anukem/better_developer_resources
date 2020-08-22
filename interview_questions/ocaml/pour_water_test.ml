
open OUnit2
open Pour_water

let tests = "test suite for pouring water" >::: [
    "the pit is at k"     >:: (fun _ -> assert_equal  [|3;3;3|] ( pour_water [|3;2;3|] 1 1 ) );
    "the height is even across the board"     >:: (fun _ -> assert_equal  [|3;4;3|] ( pour_water [|3;3;3|] 1 1) );
    "v happens multiple times and updates several values"     >:: (fun _ -> assert_equal  [|5;5;5|] ( pour_water [|3;1;3|] 1 8) );
]

let _ = run_test_tt_main tests
