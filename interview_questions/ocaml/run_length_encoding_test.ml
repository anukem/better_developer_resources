open OUnit2
open Run_length_encoding

let tests = "run length tests" >::: [
    "1"     >:: (fun _ -> assert_equal  [(4, 1);(2,2)] ( encoding [1;1;1;1;2;2] ) );
    "2"     >:: (fun _ -> assert_equal  [(4, 1)] ( encoding [1;1;1;1] ) );
]

let _ = run_test_tt_main tests
