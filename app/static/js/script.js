window.onload = function(){
                    
    window.$v = new Vue({
        el: "#cellgrid",
        methods: {
            initialize: function(size){
                state = [];
                this.current_state = (function(size){
                    for(var i = 0; i < size; i++){
                        state.push([]);
                        for (var j = 0; j < size; j++){
                            state[i].push(0);
                        }
                    }
                    return state;
                })(size)
            },
            clear: function() {
                this.current_state.forEach(function(x,i){
                    x.forEach(function(y, j){
                        window.$v.current_state[i][j] = 0;
                        window.$v.$forceUpdate();
                    });
                });
            },
            randomize: function(){
                socket.emit('Randomize', JSON.stringify(this.current_state));
            },
            advance_s: function(){
                //socket.emit('Call', {'steps':10});
                socket.emit('Call', JSON.stringify(this.current_state));
            },
            start: function(){
                //socket.emit('Call', {'steps':10});
                socket.emit('start', JSON.stringify(this.current_state));
            },
            advance: function(current_state){
                        fetch('http://localhost:5000/advance', {
                            method: 'POST',
                            headers: {
                                'content-type': 'application/json' 
                            },
                            body: JSON.stringify(current_state)
                        }).then(
                            data => data.json()
                        ).catch(error => console.error(error)
                        ).then(response => this.current_state = response);
                        
            },
            toggle_cell: function(row, cell, value){
                console.log(row + ", " + cell + ' .DepressedKeys: ' + $v.keys_depressed);
                if($v.keys_depressed !== 0){
                    this.current_state[row][cell] = value === 0 ? 1 : 0; 
                    this.$forceUpdate();
                }
                
            },
            advance_switch: function(){
                if ($v.timerid === undefined){
                    $v.timerid = setInterval(function(){
                        $v.advance_s();
                    }, $v.timeout);
                } else {
                clearInterval($v.timerid);
                $v.timerid = undefined;
                }
            },

        },
        computed: {
            cell_style: function(cell){
                
                return {
                    'background-color': cell === 0 ? wheat : black
                }
            }

        },
        data: {
            active_cell: {
                'background-color': 'black'

            },
            inactive_cell: {
                'background-color': 'wheat'
            },
            flipflop: -1,
            keys_depressed: 0,
            timerid: undefined,
            current_state: [],
            timeout: 500,
        },
    
    });
    $v.initialize(30);
    startKeypressChecker(document);

    function startKeypressChecker(document) {
        document.onkeydown = function () {
            $v.keys_depressed = 1;
        };
        document.onkeyup = function () {
            $v.keys_depressed = 0;
        };
    }
};

var socket = io.connect('http://' + document.domain + ':' + location.port);
        socket.on('connect', function() {
            //socket.emit('Call', {data: 'CallData'});
        });
        socket.on('Response', function(data){
            $v.current_state = JSON.parse(data);
            $v.flipflop *= -1; 
            console.log(typeof JSON.parsedata)
        });
         socket.on('Update', function(data){
            $v.current_state = JSON.parse(data);
            console.log(JSON.parse(data))
        });


