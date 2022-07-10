(use '[clojure.string :refer [split]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [i (create-input (read-line))
      n (take (count i) (cons 0 i))]
  (println (if (> (count (filter #(= 0 %) (map - i n))) 0)
             "YES"
             "NO")))
