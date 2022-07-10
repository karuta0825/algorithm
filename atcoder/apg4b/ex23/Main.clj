(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [_ (Integer/parseInt (read-line))
      input (create-input (read-line))]
  (->> input
       frequencies
       (apply max-key second)
       (join " ")
       println))

