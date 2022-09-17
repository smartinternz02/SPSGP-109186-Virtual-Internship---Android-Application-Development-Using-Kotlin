(function() {
  if('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
             .then(function(registration) {
             console.log('Service Worker Registered');
             return registration;
    })
    .catch(function(err) {
      console.error('Unable to register service worker.', err);
    });
    navigator.serviceWorker.ready.then(function(registration) {
      console.log('Service Worker Ready');
    });
  }
})();

// const url = 'https://flask-grocery-app.herokuapp.com/'
const url = document.location

const vm = new Vue({
  el: '#app',
  delimiters: ["[[", "]]"],
  data: {
    items: [],
    newContent: ''
  },
  mounted : function() {
    this.updateList()
  },
  methods: {
    updateList: function() {
      axios.get(url + 'list/')
      .then(function (response) {
        this.items = response.data
      }.bind(this))
    },
    newItem: function() {
      axios.post(url + 'list/', { content: this.newContent })
        .then(function (response) {
          this.newContent = '';
          this.updateList()
        }.bind(this))
    },
    updateItem: function(index) {
      axios.put(url + 'list/' + this.items[index].id, this.items[index])
        .then(function (response) {
          this.updateList()
        }.bind(this))
    },
    deleteItem: function(id) {
      axios.delete(url + 'list/' + id)
        .then(function (response) {
          this.updateList()
        }.bind(this))
    }
  }
});
