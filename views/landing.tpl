% rebase('base/base.tpl')

<form class="form-inherit" method="GET" action="/">
  <div class="mdl-grid">
      <div class="mdl-cell mdl-cell--8-col">
        <div class="mdl-textfield mdl-js-textfield">
          <input id="query" class="mdl-textfield__input" type="text" name="keywords" />
          <label class="mdl-textfield__label" for="keywords">your search goes here...</label>
        </div>
      </div>
      <div class="mdl-cell mdl-cell--4-col">
        <input type="submit" />
      </div>
  </div>
</form>
