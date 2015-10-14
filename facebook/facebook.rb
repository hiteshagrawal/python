#!/usr/bin/ruby
$has1 = Hash.new
$has2 = Hash.new
res = Hash.new
def fop(filename,has)
File.open(filename).readlines.each do |line|
   arr = line.chomp.split(/,/)
   has[arr.shift] = arr
end
end
fop("dataset1.csv",$has1)
fop("dataset2.csv",$has2)
print $has1
print $has2
$has2.each do |k, v|
if v[1] == "bipedal"
speed = ((v[0].to_f / $has1[k][0].to_f) - 1) * (($has1[k][0].to_f * 9.8) ** (0.5))
res[k] =  speed
end
end
res.sort_by{|k,v| v}.reverse.each {|k,v| puts k}
