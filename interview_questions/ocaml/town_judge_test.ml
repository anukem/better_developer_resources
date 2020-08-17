open OUnit2
open Town_judge

let tests = "test suite for finding the town judge" >::: [
    "one judge 2 people"     >:: (fun _ -> assert_equal 2 ( find_judge 2 [[1;2]] ) );
    "one judge 3 people"     >:: (fun _ -> assert_equal 3 ( find_judge 3 [[1;3];[2;3]] ) );
    "one judge 4 people"     >:: (fun _ -> assert_equal 3 ( find_judge 4 [[1;3];[1;4];[2;3];[2;4];[4;3]] ) );
    "no  judge 3 people"     >:: (fun _ -> assert_equal (-1) ( find_judge 3 [[1;3];[2;3];[3;1]] ) );
    "no  judge 4 people"     >:: (fun _ -> assert_equal (-1) ( find_judge 4 [[1;3];[2;3]] ) );
]

let _ = run_test_tt_main tests
