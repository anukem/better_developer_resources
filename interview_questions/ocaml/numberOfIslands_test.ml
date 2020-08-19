open OUnit2
open NumberOfIslands

let tests = "test suite for number of islands" >::: [
    "no islands"      >:: (fun _ -> assert_equal 0 ( num_islands [[0;0];[0;0]] ) );
    "one island"      >:: (fun _ -> assert_equal 1 ( num_islands [[1;0];[1;0]] ) );
    "two islands"     >:: (fun _ -> assert_equal 2 ( num_islands [[1;0];[0;1]] ) );
]

let _ = run_test_tt_main tests
