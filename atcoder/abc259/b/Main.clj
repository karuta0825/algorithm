(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(defn rad
  [shita]
  (* Math/PI (/ shita 180)))


(let [[x y shita] (create-input (read-line))
      s (rad shita)
      nx (- (* (Math/cos s) x) (* (Math/sin s) y))
      ny (+ (* (Math/sin s) x) (* (Math/cos s) y))]
  (println nx ny))


