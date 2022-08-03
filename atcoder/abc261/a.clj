(use '[clojure.string :refer [split join]])
(use '[clojure.set :refer [intersection]])


(defn create-input
  [arg]
  (->> (split arg #" ")
       (map #(Integer/parseInt %))))


(let [[l1 r1 l2 r2] (create-input (read-line))
      num (count (intersection
                   (set (range l1 (inc r1)))
                   (set (range l2 (inc r2)))))]
  (println (if (> num 0)
             (dec num)
             0)))


(map first '[(0 1 2 3) (10 11 12 13)])


(let [w '((\- \W \W \W) (\L \- \D \D) (\L \D \- \W) (\L \D \W \-))])


;; => ((\- \-)
;;     (\W \L)
;;     (\W \L)
;;     (\W \L)
;;     (\L \W)
;;     (\- \-)
;;     (\D \D)
;;     (\D \D)
;;     (\L \W)
;;     (\D \D)
;;     (\- \-)
;;     (\W \W)
;;     (\L \W)
;;     (\D \D)
;;     (\W \W)
;;     (\- \-))

;; => (((\- \-) (\W \L) (\W \L) (\W \L))
;;     ((\L \W) (\- \-) (\D \D) (\D \D))
;;     ((\L \W) (\D \D) (\- \-) (\W \W))
;;     ((\L \W) (\D \D) (\W \W) (\- \-)))

(mapcat identity [[3 2 1 0] [6 5 4] [9 8 7]])


;; map のmapはつかないな。
;; あぁpythonならばもっとできる気がする。これは反省だ。



(loop [n 4
       r []]
  (if (= n 0)
    (reverse r)
    (recur (dec n) (conj r (mapv (fn [v] (nth v (dec n))) '((\- \W \W \W) (\L \- \D \D) (\L \D \- \W) (\L \D \W \-)))))))


;; => ([\- \L \L \L] [\W \- \D \D] [\W \D \- \W] [\W \D \W \-])


;; => (\W \D \- \W \W \D \- \W \W \D \- \W \W \D \- \W)


(map (fn [v] (nth v 4)) '((\- \W \W \W) (\L \- \D \D) (\L \D \- \W) (\L \D \W \-)))
