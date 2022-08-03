(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [[n m x t d] (create-input (read-line))]
  (println (if (> m x)
             t
             (- t (* d (- x m))))))


(Math/cos Math/PI)


(* (Math/cos Math/PI) 2)


(defn rad
  [shita]
  (* Math/PI (/ shita 180)))


(let [one "abbaac"
      two "abbbbaaac"]
  (map-indexed (fn [i c] (take-while (fn [v] (= v c)) (drop i one))) one))


;; こういうデータを作れるとよい
;; [{"a" 1} {"b" 2} {"a" 2} {"c" 1}]
;; [{"a" 1} {"b" 4} {"a" 3} {"c" 1}]
;; 2以上のものは打ち消すことができる。1ならばアウトである

;; このようなデータ構造をつくることができるか？
;; 順番に意味をもってるので配列がただしい。
