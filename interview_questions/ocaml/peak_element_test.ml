open Peak_element
open OUnit2

let tests = "test suite for finding the peak element" >::: [
    "peak is in the first three elements"      >:: (fun _ -> assert_equal 1 ( n_solution [1;2;1;1;1;1] ) );
    "peak is in the first three elements"      >:: (fun _ -> assert_equal 1 ( find_peak_element [1;2;1;1;1;1] ) );
    "peak is the fourth element"      >:: (fun _ -> assert_equal 3 ( n_solution [1;1;1;2;1;1] ) );
    "peak is the fourth element"      >:: (fun _ -> assert_equal 3 ( find_peak_element [1;1;1;2;1;1] ) );
]

