(* # /* Given a 2D board and a word, find if the word exists in the grid. */ *)
(* # /* The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. */ *)
(* # /* Example: */ *)
(* # /* board = */ *)
(* # /* [ */ *)
(* # /*   ['A','B','C','E'], */ *)
(* # /*   ['S','F','C','S'], */ *)
(* # /*   ['A','D','E','E'] */ *)
(* # /* ] */ *)
(* # /*  */ *)
(* # /* Given word = "ABCCED", return true. */ *)
(* # /* Given word = "SEE", return true. */ *)
(* # /* Given word = "ABCB", return false. */ *)
module IntInt = struct
  type t = int * int
  let compare = compare
end

module MySet = Set.Make(IntInt)

let rec validate_path word count (i, j) arr visited =
  (* List.map (fun x -> print_string x) ["("; string_of_int i; ","; string_of_int j; ")"; "  "]; *)
  (* print_string (string_of_int count); *)
  (* print_string "\n"; *)
  if count = (String.length word) + 1 then true else
  if i < 0 ||
     j < 0 ||
     i >= Array.length arr ||
     j >= Array.length arr.(0) ||
     MySet.mem (i, j) visited then
    false
  else if word.[count - 1] <> arr.(i).(j) then false
  else validate_path word (count + 1) (i + 1, j) arr (MySet.add (i, j) visited) ||
  validate_path word (count + 1) (i - 1, j) arr (MySet.add (i, j) visited) ||
  validate_path word (count + 1) (i, j + 1) arr (MySet.add (i, j) visited) ||
  validate_path word (count + 1) (i, j - 1) arr (MySet.add (i, j) visited)

let word_search word arr =
  let found = ref false in
  for i = 0 to (Array.length arr) - 1 do
    for j = 0 to (Array.length arr.(0)) - 1 do
      if arr.(i).(j) = word.[0] && validate_path word 1 (i, j) arr MySet.empty then found := true
    done
  done;
  found
