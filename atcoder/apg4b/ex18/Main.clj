(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(defn output
  [l]
  (mapv (fn [n] (println (join " " n))) l))


(defn ops
  [l op]
  (let [i (dec (first op))
        j (dec (second op))]
    (-> l
        (update-in [i] (fn [v] (assoc (vec v) j "o")))
        (update-in [j] (fn [v] (assoc (vec v) i "x"))))))


(let [[n m] (create-input (read-line))
      inputs (map (fn [_] (create-input (read-line))) (range m))
      init (vec (partition n (repeat (* n n) "-")))]
  (output (reduce (fn [acc o] (ops acc o)) init inputs)))
