
(use '[clojure.string :refer [split join]])


(defn create-input
  [arg]
  (->> (map identity arg)))


;; どうやって転置行列をつくるろうかな？ということ
(let [num (Integer/parseInt (read-line))
      w (map (fn [_] (create-input (read-line))) (range num))]
  (println (if (some (fn [[l r]]
                       (or (and (= l \L) (= r \L))
                           (and (= l \W) (= r \W))))
                     (mapcat identity (map-indexed
                                        (fn [i row]
                                          (map-indexed (fn [j v] (list (nth (nth w i) j) (nth (nth w j) i))) row))
                                        w)))
             "incorrect"
             "correct")))


