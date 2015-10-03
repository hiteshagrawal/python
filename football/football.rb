#!/usr/bin/ruby
require 'csv'
das = Hash.new(0)
req = Hash.new(0)
CSV.foreach("football.csv") do |x|
das[x[0]] = [x[5],x[6]]
end
das.shift
das.each {|k,v|  v[0].to_i > v[1].to_i ? req[k] = v[0].to_i - v[1].to_i : req[k] = v[1].to_i - v[0].to_i }
req.sort_by{|k,v| v}.each {|k,v| puts k}
