(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [num (Integer/parseInt (read-line))
      input (map (fn [_] (create-input (read-line))) (range num))]

  (->> input
       (sort-by second)
       (map (fn [v] (join " " v)))
       (mapv println)))


(sort-by second > '((5 2) (2 7) (4 1))); => ((2 7) (5 2) (4 1))



(sort > (range 1 10)); => (9 8 7 6 5 4 3 2 1)
