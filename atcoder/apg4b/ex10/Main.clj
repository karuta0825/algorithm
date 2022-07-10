
(defn create-input
  [arg]
  (->> (clojure.string/split arg #" ")
       (map #(Integer/parseInt %))))


(defn make-bar
  [n init]
  (reduce (fn [acm _] (str acm "]")) init (take n (range))))


;; これがなんで動かないんだ？
;; (reduce #(str %1 "]") "" (take 4 (range)))

;; ２つの配列をマージしたい。
(mapv (fn [a b] (println (make-bar a b))) (create-input (read-line)) ["A:" "B:"])
