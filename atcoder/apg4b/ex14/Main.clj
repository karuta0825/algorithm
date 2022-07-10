(use '[clojure.string :refer [split]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [input (create-input (read-line))
      max (apply max input)
      min (apply min input)]
  (println (- max min)))


(let [i '(5 3 3 1 4)
      n (take (count i) (cons 0 i))]
  (println (if (> (count (filter #(= 0 %) (map - i n))) 0)
             "YES"
             "NO")))
