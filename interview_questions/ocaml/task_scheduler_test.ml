open OUnit2
open Task_scheduler

let tests = "test suite for scheduling tasks" >::: [
    "no stops"  >:: (fun _ -> assert_equal 3 ( minimium_scheduled_tasks ['a';'a';'a'] 0) );
    "one stop per task"  >:: (fun _ -> assert_equal 5 ( minimium_scheduled_tasks ['a';'a';'a'] 1) );
    "one stop per task with different letters"  >:: (fun _ -> assert_equal 3 ( minimium_scheduled_tasks ['a';'b';'a'] 1) );
]

let _ = run_test_tt_main tests

