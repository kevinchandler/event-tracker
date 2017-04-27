# Generate n number of timestamps each day in DATE_RANGES
# where n is ITERATIONS_PER_DAY
#
# active_support is included because I'm lazy

class RandomTimeGenerator
  require 'active_support/all'

  FILE_EXTENSION = 'csv'.freeze
  SEPERATOR = ','.freeze
  NEW_LINE = true
  ITERATIONS_PER_DAY = 10.freeze
  DATE_RANGES = {
    beginning: 1.month.ago.to_date,
    end: Date.today
  }.freeze


  def initialize(dates = DATE_RANGES)
    @date_ranges = dates
    puts @date_ranges
  end


  def generate_files
    filename = generate_filename
    (DATE_RANGES[:beginning]..DATE_RANGES[:end]).to_a.each do |day|
      ITERATIONS_PER_DAY.times do |iteration|
        timestamp = generate_timestamp(day.beginning_of_day.to_f,
                                       day.end_of_day.to_f)
        write_to_file(timestamp, filename)
      end
    end
  end

  private

  def generate_timestamp(time_start, time_end)
    Time.at((time_end - time_start)*rand + time_start)
  end

  def generate_filename(file_name = nil)
    file_name ||= "#{ITERATIONS_PER_DAY}.#{FILE_EXTENSION}"
  end

  def write_to_file(timestamp, file_name)
    file = File.open file_name, 'a' do |f|
      f.write "#{timestamp}#{SEPERATOR}"
      f.write "\n" if NEW_LINE
    end
  end
end


RandomTimeGenerator.new.generate_files
