/**
 * Created by sshome on 2016/2/5.
 */

var playtaskControllers = angular.module('playtaskControllers', []);


playtaskControllers.controller('allTask', ['$scope', '$http',
  function($scope, $http) {

    $http.get('http://127.0.0.1:8000/playtask/all_task').success(function(data) {
      $scope.all_task = data;
    });
}]);
  //    $scope.all_task = [
   //       {id:1,status:1,title:"英语学习",score:100,type:0,update:"2016-02-05 15:24:27"},
   //       {id:1,status:1,title:"法语学习",score:100,type:0,update:"2016-02-05 15:24:27"}
  //  ]
 // }]);

