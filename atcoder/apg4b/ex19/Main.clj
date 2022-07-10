
(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(defn output
  [l]
  (mapv (fn [n] (println (join " " n))) l))


(let [correct (map (fn [v] (map (fn [w] (* v w)) (range 1 10))) (range 1 10))
      inputs (map (fn [_] (create-input (read-line))) (range 9))
      tf (mapcat (fn [i j] (map (fn [x y] (= x y)) i j)) correct inputs)
      [true-cnt false-cnt] ((juxt (fn [i] (count (filter true? i)))
                                  (fn [i] (count (filter false? i)))) tf)]
  (output correct)
  (println true-cnt)
  (println false-cnt))


