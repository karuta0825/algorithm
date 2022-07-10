
(defn create-input
  [arg]
  (->> (clojure.string/split arg #" ")
       (map #(Integer/parseInt %))))


(let [[x a b] (create-input (read-line))
      first (inc x)
      second (* first (+ a b))
      third (* second second)
      fourth (dec third)]
  (println first)
  (println second)
  (println third)
  (println fourth))


