open OUnit2
open Run_length_encoding

let tests = "run length tests" >::: [
    "1"     >:: (fun _ -> assert_equal  [(4, 1);(2,2)] ( encoding [1;1;1;1;2;2] ) );
    "2"     >:: (fun _ -> assert_equal  [(4, 1)] ( encoding [1;1;1;1] ) );
    "4"     >:: (fun _ -> assert_equal  ["a";"a";"a";"a"] ( decode [Many (4, "a")] ) );
    "5"     >:: (fun _ -> assert_equal  ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"] ( decode [Many (4, "a"); One "b"; Many (2, "c"); Many (2, "a"); One "d"; Many (4, "e")] ) );
    "3"     >:: (fun _ -> assert_equal  [(4, "a"); (1, "b"); (2, "c"); (2, "a"); (1, "d"); (4, "e")] ( encoding ["a"; "a"; "a"; "a"; "b"; "c"; "c"; "a"; "a"; "d"; "e"; "e"; "e"; "e"] ) );
]

let _ = run_test_tt_main tests
