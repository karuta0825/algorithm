(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(defn tt
  [i ary]
  (let [f (filter #(= i (first %)) ary)]
    (if (empty? f)
      (count f)
      (reduce (fn [a v] (+ a (tt (second v) ary))) (count f) f))))


(let [number (Integer/parseInt (read-line))
      input (map-indexed (fn [i v] [v (inc i)]) (create-input (read-line)))]
  (mapv (fn [v] (println (inc (tt v input)))) (range number)))


