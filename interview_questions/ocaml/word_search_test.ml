
open OUnit2
open Word_search


let tests = "test suite for searching words" >::: [
    "word is there vertically and horizontally"  >:: (fun _ -> assert_equal (ref true) (word_search "dfsa" [|
        [| 'd';'o';'b' |];
        [| 'f';'a';'t' |];
        [| 's';'a';'t' |]
                                                                      |]));
    "word is not there"  >:: (fun _ -> assert_equal (ref false) (word_search "dog" [|
        [| 'd';'o';'b' |];
        [| 'f';'a';'t' |]
                                                                      |]));
    "word exists"  >:: (fun _ -> assert_equal (ref true) (word_search "dog" [|
        [| 'd';'o';'g' |];
        [| 'f';'a';'t' |]
                                                                      |]));
]


let _ = run_test_tt_main tests
