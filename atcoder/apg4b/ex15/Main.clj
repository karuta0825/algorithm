(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [num (Integer/parseInt (read-line))
      a (create-input (read-line))
      b (create-input (read-line))
      c (create-input (read-line))]
  (println (* (apply + a) (apply + b) (apply + c))))


;; どうやって2x2の表をつくるのかということだな。
(range 3)
(repeat 3 "-")


(let [people 3
      init (map (fn [_] (repeat people "+")) (range people))]
  (println init))
