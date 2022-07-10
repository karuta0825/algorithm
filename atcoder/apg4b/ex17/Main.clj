(use '[clojure.string :refer [split]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [[n sum] (create-input (read-line))
      i (create-input (read-line))
      j (create-input (read-line))]  (println (count (mapcat (fn [v] (filter (fn [w] (= sum (+ v w))) j)) i))))


(let [input '(0 0 1 1 4)]
  (->> (map-indexed (fn [i v] [i v]) input)
       (reduce (fn [acc v] (update-in acc [(keyword (str (second v)))] (fn [n] (conj n (first v))))) {})))


(con '(1) 2)

(update-in {:a '(1)} [:a] (fn [n] (conj n 3)))

(repeat 2 0)
