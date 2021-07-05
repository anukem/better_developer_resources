open OUnit2
open Run_length_encoding

let tests = "run length tests" >::: [
    "1"     >:: (fun _ -> assert_equal  [(4, 1);(2,2)] ( encoding [1;1;1;1;2;2] ) );
    "2"     >:: (fun _ -> assert_equal  [(4, 1)] ( encoding [1;1;1;1] ) );
    "3"     >:: (fun _ -> assert_equal  [(4, "a"); (1, "b"); (2, "c"); (2, "a"); (1, "d"); (4, "e")] ( encoding ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"] ) );
]

let _ = run_test_tt_main tests
