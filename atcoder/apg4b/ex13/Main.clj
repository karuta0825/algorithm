(use '[clojure.string :refer [split]])

(def num (Integer/parseInt (read-line)))


(defn abs
  [n]
  (max n (- n)))


(let [input (map #(Integer/parseInt %) (split (read-line) #" "))
      mean (quot (reduce + input) (count input))]
  (mapv (fn [v] (println (abs (- mean v)))) input))


;; (let [input (map #(Integer/parseInt %) (split "2 1 4" #" "))
;;       mean (quot (reduce + input) (count input))]
;;   (mapv (fn [v] (println (abs (int (- mean v))))) input))
