open OUnit2
open Find_celebrity

(* this example knows function ensures 2 is a celeb *)
let knows (x, y) =
  match x,y with
  | 0, 1 -> true
  | 0, 2 -> true
  | 1, 0 -> false
  | 1, 2 -> true
  | 2, 1 -> false
  | 2, 0 -> false
  | _ -> failwith "this persom doesn't exist"

let knows' (x, y) =
  match x,y with
  | 0, 1 -> true
  | 0, 2 -> true
  | 1, 0 -> false
  | 1, 2 -> true
  | 2, 1 -> false
  | 2, 0 -> true
  | _ -> failwith "this persom doesn't exist"

let tests = "test suite for finding a celebrity" >::: [
    "the celeb is there"      >:: (fun _ -> assert_equal 2 ( find_celebrity 2 knows ) );
    "the celeb is not there"      >:: (fun _ -> assert_equal (-1) ( find_celebrity 2 knows' ) );
]


let _ = run_test_tt_main tests
