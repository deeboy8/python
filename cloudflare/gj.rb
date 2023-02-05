require 'socket'

=begin
REQUEST FROM THE CLIENT
GET / HTTP/1.1
Host: qwasar.io
User-Agent: Quinton
Accept: */*


ANSWER FROM THE SERVER
HTTP/2 200
date: Thu, 12 Jan 2023 00:48:13 GMT
content-type: text/html; charset=UTF-8
x-powered-by: PHP/7.4.33
cf-edge-cache: cache,platform=wordpress
link: <https://qwasar.io/wp-json/>; rel="https://api.w.org/"
link: <https://qwasar.io/wp-json/wp/v2/pages/281>; rel="alternate"; type="application/json"
link: <https://qwasar.io/>; rel=shortlink
vary: Accept-Encoding
strict-transport-security: max-age=31536000; includeSubDomains; preload
x-frame-options: SAMEORIGIN
x-content-type-options: nosniff
cf-cache-status: DYNAMIC
server-timing: cf-q-config;dur=7.0000005507609e-06
report-to: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=l9qiBZIxaRjlY5AF5Z4xGpKOq%2B7trke9mhdDecBu9iRohNHSy3tDAD3HUf6tTeQpEJoJTXxc1uu3Dq2W%2FVGNTV0CFfYnkFs66cIsmisPE2sm79BkzxGYeInsET0%3D"}],"group":"cf-nel","max_age":604800}
nel: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
server: cloudflare
cf-ray: 7881e2a44a289e5f-SJC
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400


------------


=end


## OLD SCHOOL WAY

# puts "Creating the server"

# server_socket = TCPServer.new(10001)

# puts "AFTER BINDING"

# clients = []

# loop do
#     rdfds, _, _ = IO.select(clients + [server_socket], nil, nil, 1)

#     if rdfds
#         rdfds.each do |readable_socket|
#             if readable_socket == server_socket
#                 client_socket = readable_socket.accept
#                 puts "New Client On Board!!"
#                 clients << client_socket
#             else
#                 puts readable_socket.gets
#                 readable_socket.write("OK!\n")
#             end
#         end
#     end
# end

# puts "WE RECEIVED A CLIENT"

class Client
    def initialize(socket)
        @socket = socket
        @reader_buffer = []
        @writer_buffer = Queue.new
    end

    
    def reader
        @reader_buffer << @socket.gets
    end

    def start_reader
        Thread.new do
            loop do
                reader()
            end
        end
    end

    def writer
        if @writer_buffer.empty? == false
            @socket.write(@writer_buffer.pop)
        end
    end

    def start_writer
        Thread.new do
            loop do
                writer()
            end
        end
    end

    def request_completed?
        @reader_buffer.each do |line|
            if line.strip.empty?
                return true
            end
        end
        return false
    end

    def process_input
        # OPEN TCPSocket to our destination
        # Write everything we got from reader_buffer
        # answers << socket.gets
        # @writer_buffer.push answers.join("\n")

        @writer_buffer.push(File.read('qwasar_io'))
        @reader_buffer.clear
    end

    def wait_until_write_is_done
        loop do
            if @writer_buffer.empty?
                return
            end
            sleep 0.1
        end
    end

    def cleanage
        @reader_t.kill
        @writer_t.kill
        @socket.close
    end

    def run
        Thread.new do
            @reader_t = start_reader()
            @writer_t = start_writer()

            loop do
                if request_completed?
                    process_input
                    wait_until_write_is_done()
                    cleanage()
                    break
                end
                sleep 0.1
            end
        end
    end
end


puts "Creating the server"

server_socket = TCPServer.new(10001)

puts "AFTER BINDING"

clients = []

loop do
    client_socket = server_socket.accept
    puts "New Client On Board!!"

    client = Client.new(client_socket)
    client.run

    # rdfds, _, _ = IO.select(clients + [server_socket], nil, nil, 1)

    # if rdfds
    #     rdfds.each do |readable_socket|
    #         if readable_socket == server_socket
    #             clients << client_socket
    #         else
    #             puts readable_socket.gets
    #             readable_socket.write("OK!\n")
    #         end
    #     end
    # end
end

puts "WE RECEIVED A CLIENT"
